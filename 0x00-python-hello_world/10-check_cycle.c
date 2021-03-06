#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list hss a cycle in it
 * @list: A singly-linked list
 *
 * Return:  0 if it has a cycle
 *         1 otherwise
 */
int check_cycle(listint_t *list)
{
listint_t *head, *tail;

if (list == NULL || list->next == NULL)
return (0);

head = list->next;
tail = list->next->next;

while (head && tail && tail->next)
{
if (head == tail)
return (1);

head = head->next;
tail = tail->next->next;
}

return (0);
}
