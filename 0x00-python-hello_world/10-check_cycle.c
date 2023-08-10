#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Check for a singly-linked lis cycle.
 * @list: A singly-linked list
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *low, *optimal;

	if (list == NULL || list->next == NULL)
		return (0);

	low = list->next;
	optimal = list->next->next;

	while (low && optimal && optimal->next)
	{
		if (low == optimal)
			return (1);

		low = low->next;
		optimal = optimal->next->next;
	}

	return (0);
}
