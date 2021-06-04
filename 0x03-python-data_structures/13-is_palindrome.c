#include "lists.h"

/**
 * reverse_listint - reverses a singly-linked list
 * @head: a pointer to the starting node of the list to reverse
 *
 * Return: a pointer to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
  listint_t *node = *head, *next, *prev = NULL;

  while (node)
    {
      next = node->next;
      node->next = prev;
      prev = node;
      node = next;
    }

  *head = prev;
  return (*head);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: a pointer to the head of the linked list
 *
 * Return: 0 if the list is not palindrome otherwise -1
 */
int is_palindrome(listint_t **head)
{
  listint_t *temp, *rev, *mid;
  size_t size = 0, i;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  temp = *head;
  while (temp)
    {
      size++;
      temp = temp->next;
    }

  temp = *head;
  for (i = 0; i < (size / 2) - 1; i++)
    temp = temp->next;

  if ((size % 2) == 0 && temp->n != temp->next->n)
    return (0);

  temp = temp->next->next;
  rev = reverse_listint(&temp);
  mid = rev;

  temp = *head;
  while (rev)
    {
      if (temp->n != rev->n)
	return (0);
      temp = temp->next;
      rev = rev->next;
    }
  reverse_listint(&mid);

  return (1);
}
