#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Function for infinite loop
 *
 * Return: Successful execution.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Function to run the program loop
 *
 * Return: Successful execution.
 */
int main(void)
{
	int process;

	for (process = 0; process < 5; process++)
	{
		pid_t pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
