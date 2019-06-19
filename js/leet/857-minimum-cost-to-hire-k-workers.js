// Minimum Cost to Hire K Workers
// url: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
// hard
//
// Input: quality = [10,20,5], wage = [70,50,30], K = 2
// Output: 105.00000
// Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

// workers
// [0] -> 70, k = 1
// [0, 1] -> 140, k = 2
// 210
// [0] -> 10/70, k = 1
// [0, 2] -> 5/35, k = 2
// 105

function heapifyUp(heap) {
  let idx = heap.length - 1;
  while (idx > 0) {
    let parent =
      idx % 2 === 1 ? Math.floor((idx - 1) / 2) : Math.floor((idx - 2) / 2);
    if (heap[idx] < heap[parent]) {
      [heap[parent], heap[idx]] = [heap[idx], heap[parent]];
      idx = parent;
    } else {
      break;
    }
  }
}

function heapifyDown(heap) {
  let idx = 0;

  while (idx < heap.length) {
    let left_idx = idx * 2 + 1;
    let right_idx = idx * 2 + 2;

    let smallest = idx;

    if (left_idx < heap.length && heap[left_idx] < heap[idx]) {
      smallest = left_idx;
    }

    if (right_idx < heap.length && heap[right_idx] < heap[smallest]) {
      smallest = right_idx;
    }

    if (smallest !== idx) {
      [heap[smallest], heap[idx]] = [heap[idx], heap[smallest]];
      idx = smallest;
    } else {
      break;
    }
  }
}

/**
 * @param {number[]} quality
 * @param {number[]} wage
 * @param {number} K
 * @return {number}
 */
let mincostToHireWorkers = function(quality, wage, K) {
  if (K > quality.length) {
    return;
  }

  let workers = [];
  for (let i = 0; i < quality.length; i++) {
    workers.push([quality[i], wage[i], wage[i] / quality[i]]);
  }
  workers.sort((a, b) => a[2] - b[2]);

  let pool = [];
  let sumq = 0;
  let ans = Infinity;

  workers.forEach(([q, w, r]) => {
    pool.push(-q);
    heapifyUp(pool);
    sumq += q;

    if (pool.length > K) {
      let quality = pool[0];
      pool[0] = pool[pool.length - 1];
      pool.pop();
      sumq += quality;
      heapifyDown(pool);
    }

    if (pool.length === K) {
      ans = Math.min(ans, r * sumq);
    }
  });

  return ans;
};

console.log(mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2), 105);
console.log(
  mincostToHireWorkers(
    [32, 43, 66, 9, 94, 57, 25, 44, 99, 19],
    [187, 366, 117, 363, 121, 494, 348, 382, 385, 262],
    4
  ),
  1528.0
);

console.log(
  mincostToHireWorkers(
    [
      37,
      32,
      14,
      14,
      23,
      31,
      82,
      96,
      81,
      96,
      22,
      17,
      68,
      3,
      88,
      59,
      54,
      23,
      22,
      77,
      61,
      16,
      46,
      22,
      94,
      50,
      29,
      46,
      7,
      33,
      22,
      99,
      31,
      99,
      75,
      67,
      95,
      54,
      31,
      48,
      44,
      96,
      99,
      20,
      51,
      54,
      18,
      85,
      25,
      84
    ],
    [
      453,
      236,
      199,
      359,
      107,
      45,
      150,
      433,
      32,
      192,
      433,
      94,
      113,
      200,
      293,
      31,
      48,
      27,
      15,
      32,
      295,
      97,
      199,
      427,
      90,
      215,
      390,
      412,
      475,
      131,
      122,
      398,
      479,
      142,
      103,
      243,
      86,
      309,
      498,
      210,
      173,
      363,
      449,
      135,
      353,
      397,
      105,
      165,
      165,
      62
    ],
    20
  ),
  4947.75
);
