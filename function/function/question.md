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

## Question 04
請下載 `question_04` 資料夾的內容，修改 `run.py`，使 `run.py` 執行後不會出現error (不是改 `myModule.py`)

## Question 05
請下載 `question_05` 資料夾的內容，修改 `run.py`，使 `run.py` 執行後不會出現error (不是改 `myModule.py`)

## Question 06
請寫三個腳本(`.py`)，放在同一個資料夾，檔名與功能分別為:
1. `main.py`
    - 執行`module_1`內的`show_hello`
    - 執行`module_2`內的`show_now_time`
2. `module_1.py`
    - function: `show_hello`
      - output:

            hello
3. `module_2.py`
    - function: `show_now_time`
      - output: 
            
            now time is {$nowtime}
