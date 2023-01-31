# Some practice for writing class
## Question 01 : Basic class format

請定義一個 class: `Alcohol`

- propertis
  - drink_name: str
  - concentration: float (濃度)
  - kcal: float
  - ingredients: list[str,str,...]
  - bartending: bool

- functions
  - initial input:

        drink_name
        concentration
        kcal
        ingredients
        bartending

  - `show_status`
    - output:
  
          Drink name: {$drink_name}
          Concentration: {$concentration}
          kcal: {$kcal}
          Ingredients: {$ingredients}
          Bartending: {$bartending}
  
  - show_warning_sign:
    - output:

          開車不喝酒，酒後開車進監獄
  - show_if_good_to_bartending:
    - `if bartending == True`
      - output:

            This drink is good to bartending!
    - `if bartending == False`
      - output:

            This drink is bad to bartending!

## Example 01: Inherent (繼承)
請定義三個 class，分別為
- `PeriodicTable`
- `ElementFreeElectronic1`
- `ElementFreeElectronic8`

`ElementFreeElectronic1` 與 `ElementFreeElectronic8` 繼承自 `PeriodicTable`。
`ElementFreeElectronic1` 與 `ElementFreeElectronic8` 可使用同樣的function，但輸出的參數不一樣。

- basic propertis: 請參照元素週期表，設定初始值
  - `free_electronic: int`
  - `element_list: list[str,str...]`
- function:
  - `show_status`:
    - output:

          Free electronic: {$free_electronic}
          element: {$element_list}
