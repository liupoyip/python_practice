# Some practice for writing function
## Question 01

請定義一個 function

功能: 輸入兩個變數 `x`,`y`，`x`,`y`皆為 `numerical`，輸出 `x+y+87`
```
function name: plus
input: x,y
return: x+y+87
```

## Question 02
請定義一個 function，轉置多層list (類似轉置矩陣)

換句話說，轉置 `2 x 3` 的 `list`，變成 `3 x 2` 的 `list`

hint: `double for-loop`
```
function name: transpose_list

input: list[list[int,int,int], list[int,int,int]]
  
output:
------
List size before transposed: 2 x 3
result:
1,2,3,
4,5,6,
List size after transposed: 3 x 2
result:
1,4,
2,5,
3,6,
------

return: list[list[int,int], list[int,int], list[int,int]]
```

## Question 03
請定義一個 function

功能: 輸出以下格式

hint: ACSII

限制: 需要有for-loop / while loop
```
| input:65 | input:97 |
| -------- | -------- |
| output 1 | output 2 |
| A        | a        |
| BC       | bc       |
| DEF      | def      |
| GHIJ     | ghij     |
| KLMNO    | klmno    |
| PQRSTU   | pqrstu   |
| VWXYZ    | vwxyz    |
```