#ifndef __UTILS_H__
# define __UTILS_H__

// RETURN STATUS-es
// 1 = unknown problem (!) exit test for this case
// 2 = norm error (X) dont exit test for this case
// 3 = compile error (X) exit test for this case
// 4 = Leaks (X) dont exit test for this case
// 5 = test output and comparison (✔✔✔✔✔✔XX)
enum ExitCodes
{
	GOOD,
	FILE_ACCESS_ERROR,
	NORMINETTE_ERROR,
	COMPILE_ERROR,
	LEAKS
};

#endif
