#FunctionsAndVariables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man, that's enough for a party.")
    print("Get a blanket. \n")

#We can just give the function numbers directly:
cheese_and_crackers(20,30)

#We can also use variables from script:
amount_of_cheese = 15
amount_of_cheese_boxes = 25
cheese_and_crackers(amount_of_cheese, amount_of_cheese_boxes)

#We can even do math inside the function:
cheese_and_crackers(20+15, 30+10)

#And we can combine both variables and math:
cheese_and_crackers(amount_of_cheese+15, amount_of_cheese_boxes+10)

