#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *secondHalf;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *nextNode = slow->next;

		slow->next = prev;
		prev = slow;
		slow = nextNode;
	}

	if (fast != NULL)
		slow = slow->next;

	secondHalf = slow;

	while (prev != NULL && secondHalf != NULL)
	{
		if (prev->n != secondHalf->n)
			return (0);
		prev = prev->next;
		secondHalf = secondHalf->next;
	}

	return (1);
}
