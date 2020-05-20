# Snapshot Array
# https://leetcode.com/problems/snapshot-array/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class SnapshotArray:

    def __init__(self, length: int):
        self.current = [0] * length
        self.snapshots = []

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        self.snapshots.append(self.current)
        self.current = {}
        return len(self.snapshots) - 1

    def get(self, index: int, snap_id: int) -> int:
        sid = snap_id

        while True:
            if sid == 0: return self.snapshots[0][index]
            if index in self.snapshots[sid]: break
            sid -= 1

        return self.snapshots[sid][index]
