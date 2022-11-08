# someATM
* [demo](https://eunjin1.pythonanywhere.com/) is right away.
* written by eunjin(v1r4m)
* contact : choyoung7789@gmail.com

## feature / API명세서 
| parameters | 의미 | meanings| 
|------|---|---|
| cardnum | 카드번호 | card number |
| password | 암호(unhashed) | password(unhashed) |
| amountofmoney | 저금하거나 출금하고 싶은 돈의 양 | the amount of money you'd like to deposit or withdraw |
| userid | 회원정보(insert에서 조회 가능) | user information(you can check it on insert menu, because this section is insert card and check.)|
* you can have MANY card. so it is basically one-to-many relationship.
* more detailed documents are on DEMO MAIN PAGE. so check there.
* THERE IS NO GUI, you can interact this project with only URL with parameters.
* `https://eunjin1.pythonanywhere.com/insert/{cardnum}`
  *  insert card, get pw, match card number with pw
* `https://eunjin1.pythonanywhere.com/balance/{cardnum}/{password}`
  * see my balance with ONLY THAT CARD.
 * `https://eunjin1.pythonanywhere.com/balance_all/{userid}/{password}`
   * see my all balance with ALL MY CARD.
 * `https://eunjin1.pythonanywhere.com/deposit/{cardnum}/{password}/{amountofmoney}`
   * deposit in that card
 * `https://eunjin1.pythonanywhere.com/Withdraw/{cardnum}/{password}/{amountofmoney}`
   * withdraw from that card
 * `https://eunjin1.pythonanywhere.com/newregister/{userId}/{cardNum}/{password}`
   * register new.
