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
	listint_t *current = *head, *reversed = NULL, *temp;
	int isPalindrome = 1;

	while (current != NULL)
	{
		temp = malloc(sizeof(listint_t));
		if (temp == NULL)
			return (0);
		temp->n = current->n;
		temp->next = reversed;
		reversed = temp;
		current = current->next;
	}

	current = *head;
	while (current != NULL && reversed != NULL)
	{
		if (current->n != reversed->n)
		{
			isPalindrome = 0;
			break;
		}
		current = current->next;
		reversed = reversed->next;
	}

	while (reversed != NULL)
	{
		temp = reversed;
		reversed = reversed->next;
		free(temp);
	}

	return (isPalindrome);
}

