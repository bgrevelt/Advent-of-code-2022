def get_start_of_frame_index(stream, sof_length):
    for n in range(len(stream)-sof_length):
        if len(set(stream[n:n+sof_length])) == sof_length:
            return n + sof_length
    raise Exception("SOF not found")

assert get_start_of_frame_index('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
assert get_start_of_frame_index('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert get_start_of_frame_index('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert get_start_of_frame_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert get_start_of_frame_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11

assert get_start_of_frame_index('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert get_start_of_frame_index('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert get_start_of_frame_index('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert get_start_of_frame_index('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert get_start_of_frame_index('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26

with open('input.txt') as f:
    txt = f.read()
    print(get_start_of_frame_index(txt,4))
    print(get_start_of_frame_index(txt, 14))