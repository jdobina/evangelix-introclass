/int$/N
s/^\s*int\s\+main\s*(.*)/#ifndef ANGELIX_OUTPUT\n#define ANGELIX_OUTPUT(type, expr, id) expr\n#endif\nint main(int argc, char *argv[])/
/printf.*Enter an/d
s/\(^.*\)scanf\s*("%s",\s*\(.*\)\s*);/\1strcpy(\2, argv[1]);/
s/printf.*Check sum is.*,\s*\(.\+\)\s*);/printf("%c\\n", ANGELIX_OUTPUT(char, \1, "stdout"));/
s/\r$//
s/\bdouble\b/int/g
s/\bfloat\b/int/g
