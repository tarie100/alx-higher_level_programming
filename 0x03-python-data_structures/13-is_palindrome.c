#include"lists.h"
/**
 * reverse_list - reverses list
 * @head: 1st node
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *previous = NULL;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}
/**
 * is_palindrome - checks if list is palindrome
 * @head: 1st node
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL ||(*head)->next == NULL)
	{
		return (1);
	}
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size/2) - 1; i++)
	{
		temp = temp->next;
	}
	if ((size % 2) == 0 && temp->n != temp->next->n)
	{
	       return (0);
	}
	temp = temp->next->next;
	rev = reverse_list(&temp);
	mid = rev;
	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_list(&mid);
	return (1);
}
