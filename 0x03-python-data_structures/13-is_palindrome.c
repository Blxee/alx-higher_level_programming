#include "lists.h"
#include <stdlib.h>

/**
 * list_len - retrives the length of a linked list
 *
 * @head: the head of the list
 *
 * Return: the length of the list
 */
unsigned int list_len(const listint_t *head)
{
	unsigned int len = 0;

	if (head == NULL)
		return (len);
	len++;
	while (head->next)
	{
		head = head->next;
		len++;
	}
	return (len);
}

/**
 * is_palindrome - determines whether a list is a palindrome (mirrored)
 *
 * @head: the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 elsewise
 */
int is_palindrome(listint_t **head)
{
	listint_t **half, *left, *right, *temp;
	int len, i;

	if (head == NULL || *head == NULL)
		return (1);

	len = list_len(*head);
	half = malloc((len / 2) * sizeof(*half));
	if (half == NULL)
		return (0);

	temp = *head;
	for (i = 0; i < len / 2; i++)
	{
		half[i] = temp;
		left = temp;
		temp = temp->next;
	}
	right = (len % 2 == 0) ? temp : temp->next;

	for (i -= 2; i >= -1; i--)
	{
		printf("l: %d, r: %d\n", left->n, right->n);
		if (left->n != right->n)
		{
			free(half);
			return (0);
		}
		if (i >= 0)
		{
			left = half[i];
			right = right->next;
		}
	}
	free(half);
	return (1);
}
