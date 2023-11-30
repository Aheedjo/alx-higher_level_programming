#include "lists.h"

/**
* check_cycle - A function in C that checks if a singly
* linked list has a cycle in it.
* @list: a pointer to the head of the ll
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *curr, *check;

    if (list == NULL || list->next == NULL)
        return (0);
    curr = list;
    check = curr->next;

    while (curr != NULL && check->next != NULL
        && check->next->next != NULL)
    {
        if (curr == check)
            return (1);
        curr = curr->next;
        check = check->next->next;
    }
    return (0);
}
