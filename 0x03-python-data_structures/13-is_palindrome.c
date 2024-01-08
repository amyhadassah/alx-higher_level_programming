#include "lists.h"
#include <stdbool.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the start of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * compare_lists - compares two lists
 * @head1: first list
 * @head2: second list
 * Return: true if lists are identical, otherwise false
 */
bool compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (false);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	if (temp1 == NULL && temp2 == NULL)
		return (true);

	return (false);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list to be checked
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *midnode = NULL;
	bool res = true;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_of_slow->next = NULL;
		reverse_list(&second_half);
		res = compare_lists(*head, second_half);

		if (midnode != NULL)
		{
			prev_of_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow->next = second_half;
	}

	return (res);
}
