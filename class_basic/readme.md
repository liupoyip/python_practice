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
  - show_status
    - output:
  
          Drink name: {$drink_name}
          Concentration: {$concentration}
          Kcal: {$kcal}
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

## Example 01: Inherent
請定義三個 class，分別為
- `PeriodicTable`
- `ElementFreeElectronic1`
- `ElementFreeElectronic8`

`ElementFreeElectronic1` 與 `ElementFreeElectronic8` 繼承自 `PeriodicTable`。
`ElementFreeElectronic1` 與 `ElementFreeElectronic8` 可使用同樣的function，但輸出的參數不一樣。