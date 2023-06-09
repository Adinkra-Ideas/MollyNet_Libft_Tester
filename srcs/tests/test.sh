# Generate output from user
cc -Wall -Wextra -Werror -D DEEPTHOUGHTS_DIR='"../deepthought/"' -D OUT_FILE='"isalpha_user_out"' -D FUNC="ft_isalpha" isalpha.c
./a.out

# Generate output from STD
cc -Wall -Wextra -Werror -D DEEPTHOUGHTS_DIR='"../deepthought/"' -D OUT_FILE='"isalpha_std_out"' -D FUNC="isalpha" isalpha.c
./a.out

rm -f a.out