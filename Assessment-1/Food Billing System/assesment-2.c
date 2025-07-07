#include <stdio.h>


void showMenu() 
{
    printf("\n========== MENU ==========\n");
    printf("Code\tItem\t\t\tPrice\n");
    printf("1\tButter Sandwich\tRs. 250\n");
    printf("2\tGrill Sandwich\t\tRs. 150\n");
    printf("3\tPasta\t\t\tRs. 120\n");
    printf("4\tCheese Sandwich\t\tRs. 100\n");
    printf("5\tCoffee\t\t\tRs. 80\n");
    printf("==========================\n");
}

int main() 
{
    int item, quantity;
    char moreOrder;
    float totalBill = 0;

  
    int butterQty = 0, grillQty = 0, pastaQty = 0, cheeseQty = 0, coffeeQty = 0;

    do 
    {
        showMenu();

        printf("Enter the item code you want to order: ");
        scanf("%d", &item);

        printf("Enter quantity: ");
        scanf("%d", &quantity);

        switch (item) 
        {
            case 1:
                totalBill += 250 * quantity;
                butterQty += quantity;
                printf("You ordered %d Butter Sandwich(s).\n", quantity);
                break;
            case 2:
                totalBill += 150 * quantity;
                grillQty += quantity;
                printf("You ordered %d Grill Sandwich(s).\n", quantity);
                break;
            case 3:
                totalBill += 120 * quantity;
                pastaQty += quantity;
                printf("You ordered %d Pasta(s).\n", quantity);
                break;
            case 4:
                totalBill += 100 * quantity;
                cheeseQty += quantity;
                printf("You ordered %d Cheese Sandwich(es).\n", quantity);
                break;
            case 5:
                totalBill += 80 * quantity;
                coffeeQty += quantity;
                printf("You ordered %d Coffee(s).\n", quantity);
                break;
            default:
                printf("Invalid choice. Please select a valid item.\n");
        }

        printf("Do you want to order more? (Y/N): ");
        scanf(" %c", &moreOrder);  // Note the space before %c to consume newline

    } while (moreOrder == 'Y' || moreOrder == 'y');

    
    printf("\n========== BILL ==========\n");
    printf("Thank you for your order!\n");

    if (butterQty > 0)
        printf("Butter Sandwich x %d = Rs. %d\n", butterQty, 250 * butterQty);
    if (grillQty > 0)
        printf("Grill Sandwich x %d = Rs. %d\n", grillQty, 150 * grillQty);
    if (pastaQty > 0)
        printf("Pasta x %d = Rs. %d\n", pastaQty, 120 * pastaQty);
    if (cheeseQty > 0)
        printf("Cheese Sandwich x %d = Rs. %d\n", cheeseQty, 100 * cheeseQty);
    if (coffeeQty > 0)
        printf("Coffee x %d = Rs. %d\n", coffeeQty, 80 * coffeeQty);

    printf("--------------------------\n");
    printf("Total Bill: Rs. %.2f\n", totalBill);
    printf("==========================\n");
    printf("Please visit again!\n");

    return 0;
}
