import time
import logging
from datetime import datetime
from parsing import parse_demo_files_in_batches
from populate_functions import (
    populate_match, populate_rounds, populate_bomb_events,
    populate_frames, populate_player_frames, populate_kills,
    populate_damages, populate_grenades, populate_flashes,
    populate_weapon_fires
)
from remote_db import execute_remote_sql
from sql_commands import (
    insert_single_match_sql, insert_single_round_sql, insert_single_kill_sql,
    insert_single_damage_sql, insert_single_grenade_sql, insert_single_flash_sql,
    insert_single_weapon_fire_sql, insert_single_bomb_event_sql, insert_single_frame_sql,
    insert_single_player_frame_sql
)
from config import log_file_path
from log_utils import log_timing_and_count
from utility_functions import get_deep_size, batch_insert, clean_parsed_data
from concurrent.futures import ThreadPoolExecutor
import sys

# Set up logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

overall_start_time = time.time()

def insert_data(parsed_data, thread_id, thread_log_path):
    match = parsed_data['matchID']
    rounds_list = parsed_data['rounds']
    bombs_list = parsed_data['bombEvents']
    frames_list = parsed_data['frames']
    player_frames_list = parsed_data['playerFrames']
    kills_list = parsed_data['kills']
    damages_list = parsed_data['damages']
    grenades_list = parsed_data['grenades']
    weapon_fires_list = parsed_data['weaponFires']
    flashes_list = parsed_data['flashes']

    # Timing for calculating deep sizes
    start_time = time.time()
    rounds_storage = get_deep_size(rounds_list)
    kills_storage = get_deep_size(kills_list)
    damages_storage = get_deep_size(damages_list)
    grenades_storage = get_deep_size(grenades_list)
    flashes_storage = get_deep_size(flashes_list)
    weapon_fires_storage = get_deep_size(weapon_fires_list)
    bomb_events_storage = get_deep_size(bombs_list)
    frames_storage = get_deep_size(frames_list)
    player_frames_storage = get_deep_size(player_frames_list)
    deep_size_duration = time.time() - start_time
    total_storage = (rounds_storage + kills_storage + damages_storage +
                     grenades_storage + flashes_storage + weapon_fires_storage +
                     bomb_events_storage + frames_storage + player_frames_storage)
    
    print(f"Thread {thread_id} calculated deep sizes in {deep_size_duration:.2f} seconds.")
    print(f"Thread {thread_id} total storage is {total_storage} bytes.")

    # Inserting data
    start_time = time.time()
    execute_remote_sql([insert_single_match_sql(match)], log_file_path)
    log_timing_and_count(thread_log_path, 'Match Insertion', time.time() - start_time, 1)

    start_time = time.time()
    execute_remote_sql(batch_insert(rounds_list, insert_single_round_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Rounds Insertion', time.time() - start_time, len(rounds_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(kills_list, insert_single_kill_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Kills Insertion', time.time() - start_time, len(kills_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(damages_list, insert_single_damage_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Damages Insertion', time.time() - start_time, len(damages_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(grenades_list, insert_single_grenade_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Grenades Insertion', time.time() - start_time, len(grenades_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(flashes_list, insert_single_flash_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Flashes Insertion', time.time() - start_time, len(flashes_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(weapon_fires_list, insert_single_weapon_fire_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Weapon Fires Insertion', time.time() - start_time, len(weapon_fires_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(bombs_list, insert_single_bomb_event_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Bomb Events Insertion', time.time() - start_time, len(bombs_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(frames_list, insert_single_frame_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Frames Insertion', time.time() - start_time, len(frames_list))

    start_time = time.time()
    execute_remote_sql(batch_insert(player_frames_list, insert_single_player_frame_sql), log_file_path)
    log_timing_and_count(thread_log_path, 'Player Frames Insertion', time.time() - start_time, len(player_frames_list))

    overall_duration = time.time() - overall_start_time
    logging.info(f'Thread {thread_id} Overall Insertion Time: {overall_duration:.2f} seconds')

def main():
    overall_start_time = time.time()
    
    # Example usage
    directory_path = 'D:\\CS_DEMOS'
    start_time = time.time()
    parsed_data_list = parse_demo_files_in_batches(directory_path, 12, 12)
    #parsed_data_list = parse_demo_files(directory_path, parse_first_only=True)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Parsed {len(parsed_data_list)} demo files in {duration:.2f} seconds.")
    parsed_datas = []

    start_time = time.time()
    for i, parsed_data in enumerate(parsed_data_list):
        print("i = {}".format(i))
        print("keys are {}".format(list(parsed_data_list[i].keys())))
        parsed_data_list[i] = clean_parsed_data(parsed_data_list[i])
        parsed_datas.append({
            'matchID': populate_match(parsed_data),
            'rounds': populate_rounds(parsed_data),
            'bombEvents': populate_bomb_events(parsed_data),
            'frames': populate_frames(parsed_data, parsed_data['matchID']),
            'playerFrames': populate_player_frames(parsed_data),
            'kills': populate_kills(parsed_data),
            'damages': populate_damages(parsed_data),
            'grenades': populate_grenades(parsed_data),
            'weaponFires': populate_weapon_fires(parsed_data),
            'flashes': populate_flashes(parsed_data),
        })

        # rounds_list = populate_rounds(parsed_data_list[i])
        # bombs_list = populate_bomb_events(parsed_data_list[i])
        # frames_list = populate_frames(parsed_data_list[i], parsed_data_list[i]['matchID'])
        # player_frames_list = populate_player_frames(parsed_data_list[i])
        # kills_list = populate_kills(parsed_data_list[i])
        # damages_list = populate_damages(parsed_data_list[i])
        # grenades_list = populate_grenades(parsed_data_list[i])
        # weapon_fires_list = populate_weapon_fires(parsed_data_list[i])
        # flashes_list = populate_flashes(parsed_data_list[i])
    # parsed_data = clean_parsed_data(parsed_datas)

    print(len(parsed_datas))
    print(type(parsed_datas[0]))

    # # Timing for populating lists
    # match = populate_match(parsed_data)
    # rounds_list = populate_rounds(parsed_data)
    # bombs_list = populate_bomb_events(parsed_data)
    # frames_list = populate_frames(parsed_data, parsed_data['matchID'])
    # player_frames_list = populate_player_frames(parsed_data)
    # kills_list = populate_kills(parsed_data)
    # damages_list = populate_damages(parsed_data)
    # grenades_list = populate_grenades(parsed_data)
    # weapon_fires_list = populate_weapon_fires(parsed_data)
    # flashes_list = populate_flashes(parsed_data)
    end_time = time.time()
    populate_duration = end_time - start_time
    print(f"Cleaned + Populated all lists in {populate_duration:.2f} seconds.")

    # Using ThreadPoolExecutor to insert data in parallel
    start_time = time.time()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file_path = "insertion_log.txt" + timestamp
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        for i, parsed_data in enumerate(parsed_datas):
            futures.append(executor.submit(insert_data, parsed_data, i, log_file_path))
        
        # Wait for all threads to complete
        for future in futures:
            future.result()

    overall_end_time = time.time()
    overall_duration = overall_end_time - overall_start_time
    logging.info(f'Overall Insertion Time: {overall_duration:.2f} seconds')

    

    # # Timing for calculating deep sizes
    # start_time = time.time()
    # rounds_storage = get_deep_size(rounds_list)
    # print("Number of records in rounds list is {}".format(len(rounds_list)))

    # kills_storage = get_deep_size(kills_list)
    # print("Number of records in kills list is {}".format(len(kills_list)))

    # damages_storage = get_deep_size(damages_list)
    # print("Number of records in damages list is {}".format(len(damages_list)))

    # grenades_storage = get_deep_size(grenades_list)
    # print("Number of records in grenades list is {}".format(len(grenades_list)))

    # flashes_storage = get_deep_size(flashes_list)
    # print("Number of records in flashes list is {}".format(len(flashes_list)))

    # weapon_fires_storage = get_deep_size(weapon_fires_list)
    # print("Number of records in weapon fires list is {}".format(len(weapon_fires_list)))

    # bomb_events_storage = get_deep_size(bombs_list)
    # print("Number of records in bomb events list is {}".format(len(bombs_list)))

    # frames_storage = get_deep_size(frames_list)
    # print("Number of records in frames list is {}".format(len(frames_list)))

    # player_frames_storage = get_deep_size(player_frames_list)
    # print("Number of records in player frames list is {}".format(len(player_frames_list)))
    # end_time = time.time()
    # deep_size_duration = end_time - start_time
    # print(f"Calculated deep sizes for all lists in {deep_size_duration:.2f} seconds.")

    # total_storage = (rounds_storage + kills_storage + damages_storage +
    #                  grenades_storage + flashes_storage + weapon_fires_storage +
    #                  bomb_events_storage + frames_storage + player_frames_storage)
    
    # print("total storage is {} bytes".format(total_storage))

    # # Inserting data
    # start_time = time.time()
    # execute_remote_sql([insert_single_match_sql(match)], log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Match Insertion', end_time - start_time, 1)

    # start_time = time.time()
    # execute_remote_sql(batch_insert(rounds_list, insert_single_round_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Rounds Insertion', end_time - start_time, len(rounds_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(kills_list, insert_single_kill_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Kills Insertion', end_time - start_time, len(kills_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(damages_list, insert_single_damage_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Damages Insertion', end_time - start_time, len(damages_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(grenades_list, insert_single_grenade_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Grenades Insertion', end_time - start_time, len(grenades_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(flashes_list, insert_single_flash_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Flashes Insertion', end_time - start_time, len(flashes_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(weapon_fires_list, insert_single_weapon_fire_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Weapon Fires Insertion', end_time - start_time, len(weapon_fires_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(bombs_list, insert_single_bomb_event_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Bomb Events Insertion', end_time - start_time, len(bombs_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(frames_list, insert_single_frame_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Frames Insertion', end_time - start_time, len(frames_list))

    # start_time = time.time()
    # execute_remote_sql(batch_insert(player_frames_list, insert_single_player_frame_sql), log_file_path)
    # end_time = time.time()
    # log_timing_and_count(log_file_path, 'Player Frames Insertion', end_time - start_time, len(player_frames_list))

    # overall_end_time = time.time() 
    # overall_duration = overall_end_time - overall_start_time
    # logging.info(f'Overall Insertion Time: {overall_duration:.2f} seconds')

if __name__ == "__main__":
    main()
