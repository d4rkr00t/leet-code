// Max Sum Contiguous Subarray
// #url: https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
// Solution: https://gist.github.com/mycodeschool/4b0b01e1d08932066301

function maxSubArray(nums) {
  var ans = nums[0];
  var sum = 0;

  for (var i = 0; i < nums.length; i++) {
    ans = Math.max(ans, nums[i]);
  }

  if (ans < 0) return ans;

  ans = 0;

  for (var i = 1; i < nums.length; i++) {
    if (sum + nums[i] > 0) {
      sum += nums[i];
    } else {
      sum = 0;
    }

    ans = Math.max(sum, ans);
  }

  return ans;
}

console.log(
  "Expected: 6",
  "Actual:",
  maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
);
