## <span style="color:pink"> **Practice 01-1** </span>

請完成 `main.py` 兩個功能：

1. 執行 `main.py`時，會將 `data` 內的 `*.csv` 自動找出來，放在一個 `list` 中
2. import `modules` 底下的 `hello.py` 和 `world.py`

整體檔案結構如下
```
practice_01/
|-- main.py
|-- data/
|   |-- data_00.csv
|   |-- data_01.csv
|   |-- data_02.csv
|-- modules/
|   |-- hello.py
|   |-- world.py
```

hint: `os.listdir`

PS: 禁止使用絕對路徑

## <span style="color:pink"> **Practice 01-2** </span>

1. 承 Practice 01-1，新增 `main.py` 的功能: 在 `./data` 內新增一個 `readme.txt`，請用判斷的方式，將 `*.txt` 剔除，只留下 `*.csv`
   - 備註: 請不要用 `index` 直接刪除指定位置的資料
2. 承 Practice 01-1，在 `main.py` 的上一層新增一個 `sdk` 資料夾，請 import `sdk` 底下的 module

```
practice_01/
|-- main.py
|-- data/
|   |-- data_00.csv
|   |-- data_01.csv
|   |-- data_02.csv
|   |-- readme.txt
|-- modules/
|   |-- hello.py
|   |-- world.py
sdk/
|-- foo.py
```
hint 1: `os.path.splitext`

hint 2: `os.listdir`, `sys.path`, `sys.path.append`
 

PS: 禁止使用絕對路徑