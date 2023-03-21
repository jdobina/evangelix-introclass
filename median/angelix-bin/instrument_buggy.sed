s/^\s*int main\s*(\s*)/#include <stdlib.h>\n#ifndef ANGELIX_OUTPUT\n#define ANGELIX_OUTPUT(type, expr, id) expr\n#endif\nint main(int argc, char *argv[])/
/printf.*Please enter 3 numbers separated by spaces/d
s/\(^.*\)scanf.*%d\s*%d\s*%d.*,\s*&\(.*\),\s*&\(.*\),\s*&\(.*\)\s*);/\1\2 = atoi(argv[1]);\n\1\3 = atoi(argv[2]);\n\1\4 = atoi(argv[3]);/
s/printf.*%d is the median.*,\s*\(.\+\)\s*);/printf("%d\\n", \1);/
