// Longest palindromic substr
// #url: https://leetcode.com/problems/longest-palindromic-substring/
// #medium
//
// Example 1:
//   Input: "babad"
//   Output: "bab"
//   Note: "aba" is also a valid answer.
//
// Example 2:
//   Input: "cbbd"
//   Output: "bb"
//
// Questions to ask:
//   TBD
//
// Things to consider:
//   1. empty array
//   2. array with 1 item
//   3. even palindromes
//   4. odd palindromes
//
// Solution:
//   1. For each point find possible palindrome
//   2. if s[i] s[i+1] are equal it's possible palindrome with even number of characters

fn is_palindrome(s: &[u8]) -> bool {
  let s1 = s.clone().to_owned();
  let mut s2 = s.clone().to_vec();
  s2.reverse();
  return s1 == s2.to_owned();
}

fn longest_palindrome(s: String) -> String {
  let byte_str = s.as_bytes();

  if byte_str.len() <= 1 || is_palindrome(&byte_str) {
    return s.clone();
  }

  let mut range = (0, 0);

  for i in 0..byte_str.len() - 1 {
    let mut s = i;
    let mut e = s;

    // Extend e if the same char
    while e < byte_str.len() - 1 && byte_str[e + 1] == byte_str[i] {
      e = e + 1;
    }

    loop {
      if is_palindrome(&byte_str[s..e + 1]) {
        if range.1 - range.0 < e - s {
          range = (s, e);
        }
        s = if s == 0 { s } else { s - 1 };
        e = if e == byte_str.len() - 1 { e } else { e + 1 };
      } else {
        break;
      }
    }
  }

  String::from_utf8(byte_str[range.0..(range.1 + 1)].to_vec()).unwrap()
}

fn main() {
  println!("{:?}", longest_palindrome(String::from("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd")));
}


#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_1() {
    assert_eq!(
      longest_palindrome(String::from("babad")),
      String::from("bab")
    );
  }

  #[test]
  fn test_2() {
    assert_eq!(longest_palindrome(String::from("cbbd")), String::from("bb"));
  }

  #[test]
  fn test_3() {
    assert_eq!(longest_palindrome(String::from("b")), String::from("b"));
  }

  #[test]
  fn test_4() {
    assert_eq!(longest_palindrome(String::from("ac")), String::from("a"));
  }

  #[test]
  fn test_5() {
    assert_eq!(
      longest_palindrome(String::from("abadd")),
      String::from("aba")
    );
  }

  #[test]
  fn test_6() {
    assert_eq!(longest_palindrome(String::from("bb")), String::from("bb"));
  }
}
