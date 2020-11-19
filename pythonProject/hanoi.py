def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    ######## 원판의 개수가 1개라면 '1번 원판을 1번기둥에서 3번 기둥으로 이동' ############
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    ######## 원판의 개수가 2개라면 ###########
    # 그 전에 다른 기둥을 생성
    other_peg = 6 - start_peg - end_peg

    # 가장위에있는 원판을 두 번째 기둥에다가 놓음(반복)재귀
    hanoi(num_disks - 1, start_peg, other_peg) # 112  #212이면 112로 돌아옴
    # 가장 큰 원판을 바지막 기둥에다가 놓음(한번만)
    move_disk(num_disks, start_peg, end_peg)
    # 가장 위에있는 원판을 마지막 기둥에다가 놓음(반복)재귀
    hanoi(num_disks - 1, other_peg, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(1, 1, 3)
print('')
hanoi(2, 1, 3)
print('')
hanoi(3, 1, 3)