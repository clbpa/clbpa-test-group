# Đề bài

- Thời gian chay: `4000ms`
- Phân biệt hoa/thường: `Có`

## Bài 1 (BAI-1)

Viết chương trình tìm `UCLN`[^1] và `BCNN`[^2] của 2 số nguyên dương.

### Đầu vào

Gồm 2 số nguyên dương `a` và `b` cách nhau bởi `dấu cách`. $(0 < a, b <= 10^9)$

### Đầu ra

Gồm 2 số lần lượt là `UCLN` và `BCNN` của 2 số `a` và `b` cách nhau bởi `dấu cách`.

### Ví dụ

| Input   | Output   |
| ------- | -------- |
| `30 40` | `10 120` |

## Bài 2 (BAI-2)

Viết chương trình kiểm tra xem 1 số có phải là số hay không.

### Đầu vào

Dòng duy nhất chứ 1 số nguyên dương `n`. $(n <= 2 <= 10^9)$

### Đầu ra

Nếu `n` là số nguyên dương thì xuất ra `true`, nếu không phải thì xuất ra `false`.

### Ví dụ

| Input | Output  |
| ----- | ------- |
| `2`   | `true`  |
| `4`   | `false` |

## Bài 3 (BAI-3)

Cho 1 xâu kí tự, hãy nén xâu đã cho theo quy tắc:

- Tách các xâu con có các kí tự liên tiếp giống nhau. _(Vd: `"aabbca"` -> `["aa", "bb", "c", "a"]`)_
- Nếu xâu con độ dài lớn hơn `1` thì thay xâu đó bằng độ dài của xâu con với kí tự lập lại _(Vd: `"aaa"` -> `"3a"`)_
- Cuối cùng, ghép các xâu con đã nén theo thứ tự ban đầu để tạo ra xâu kết quả.

### Đầu vào

Dòng duy nhất chứa 1 xâu kí tự `s`. $(1<= s.length <= 255)$

### Đầu ra

Xâu kí tự đã được nén.

### Ví dụ

| Input    | Output  |
| -------- | ------- |
| `aabbbc` | `2a3bc` |

[^1]: Ước số chung lớn nhất
[^2]: Bội số chung nhỏ nhất
