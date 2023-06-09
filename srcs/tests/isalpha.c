# include <stdio.h>
# include <unistd.h>
# include <string.h>
# include <fcntl.h>
# include <stdlib.h>
# include <ctype.h>

# include "./includes/utils.h"

int	ft_isalpha(int c)
{
	if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
		return (21);
	else
		return (0);
}

int main() {
	int		fd;
	char	*filepath = DEEPTHOUGHTS_DIR OUT_FILE;
	int		param1[] =	{'a' - 1, 'z' + 1, 'a', 'z', 'A' - 1, 'Z' + 1, 'Z', 0,
							'c', 'j', 'm', 'w'
						};

	fd = open(filepath, O_CREAT | O_TRUNC | O_WRONLY, 0644);
	if ( fd == -1 )
		return(FILE_ACCESS_ERROR);

	dup2(fd, 1);
	dup2(fd, 2);
	
	for ( int i = sizeof(param1) / sizeof(int) - 1; i >= 0; --i) {
		printf("%i\n", FUNC(param1[i]));
	}

	close(fd);

	return (GOOD);
}

// TODO check how signal(SIGSEGV, sigsegv) can be used to catch/workwith segmentation fault
// python should be able to combine the files and their corresponding test file
