// Median of Two Sorted Arrays
// #url: https://leetcode.com/problems/median-of-two-sorted-arrays/
// #hard
// #binary_search
//
// Example:
// nums1 = [1, 3]
// nums2 = [2]
// The median is 2.0
//
// Example:
// nums1 = [1, 2]
// nums2 = [3, 4]
// The median is (2 + 3)/2 = 2.5
//
// Questions to ask:
//   1. Can be empty?
//   2. Runtime complexity?
//      The overall run time complexity should be O(log (m+n)).
//
// Algo:
//   Step 1:
//     [1, 3, 5], [2, 4, 6, 8]
//     l1 = 4
//     l2 = 3
//     imin = 0
//     imax = 4
//     half_len = (4 + 3 + 1) / 2 = 4
//
//   Step 2 (while iter 1):
//     i = (0 + 4) / 2 = 2
//     j = 4 - 2 = 2
//     [2, 4, (6), 8], [1, 3, (5)],
//             i               j
//     imin = 1 + 1 = 2
//
//   Step 3 (while iter 1):
//     i = (2 + 3) / 2 = 2
//     j = 4 - 2 = 2
//     [1, 3, (5)], [2, 4, (6), 8]
//             i           j
//     max_left = max(3, 4) = 4

use std::cmp;

fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
  let (arr1, arr2) = if nums1.len() > nums2.len() {
    (nums1, nums2)
  } else {
    (nums2, nums1)
  };
  let arr1_len = arr1.len();
  let arr2_len = arr2.len();
  let mut imin = 0;
  let mut imax = arr1_len;
  let half_len = (arr1_len + arr2_len + 1) / 2;

  while imin <= imax {
    let i = (imin + imax) / 2;
    let j = half_len - i;

    println!("i: {:?}, j: {:?}, imax: {:?}", i, j, imax);

    if i < imax && arr2[j - 1] > arr1[i] {
      imin = i + 1;
    } else if i > imin && arr1[i - 1] > arr2[j] {
      imax = i - 1;
    } else {
      let max_left: i32;
      if i == 0 {
        max_left = arr2[j - 1];
      } else if j == 0 {
        max_left = arr1[i - 1];
      } else {
        max_left = cmp::max(arr1[i - 1], arr2[j - 1]);
      }


      if (arr1_len + arr2_len) % 2 == 1 {
        return max_left as f64;
      }

      let min_right: i32;
      if i == arr1_len {
        min_right = arr2[j];
      } else if j == arr2_len {
        min_right = arr1[i];
      } else {
        min_right = cmp::min(arr2[j], arr1[i]);
      }

      return ((max_left + min_right) as f64) / 2.0;
    }
  }

  0.0
}

fn main() {
  println!(
    "{:?}",
    find_median_sorted_arrays(vec![1, 3, 5], vec![2, 4, 6, 8])
  );
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_median_n1n2() {
    assert_eq!(find_median_sorted_arrays(vec![1, 2], vec![3, 4]), 2.5);
  }

  #[test]
  fn test_median_n2n1() {
    assert_eq!(find_median_sorted_arrays(vec![3, 4], vec![1, 2]), 2.5);
  }

  #[test]
  fn test_median_n1n2_overlap() {
    assert_eq!(
      find_median_sorted_arrays(vec![1, 3, 5], vec![2, 4, 6, 8]),
      4.0
    );
  }
}
