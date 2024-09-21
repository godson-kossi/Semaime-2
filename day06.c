#include <criterion/criterion.h>
#include <string.h>

// Function to compute the result color based on two adjacent colors.
char combine_colors(char a, char b) {
    if (a == b) return a;
    if ((a == 'R' && b == 'G') || (a == 'G' && b == 'R')) return 'B';
    if ((a == 'R' && b == 'B') || (a == 'B' && b == 'R')) return 'G';
    if ((a == 'G' && b == 'B') || (a == 'B' && b == 'G')) return 'R';
}

// Function to reduce the color triangle.
char triangle(const char *clrs) {
    int len = strlen(clrs);
    char current[len + 1];
    strcpy(current, clrs);

    while (len > 1) {
        for (int i = 0; i < len - 1; ++i) {
            current[i] = combine_colors(current[i], current[i + 1]);
        }
        len--;
    }
    return current[0];
}

// Testing helper function
static void assert_data(const char *clrs, char expected) {
    char actual = triangle(clrs);
    if (actual != expected) {
        cr_assert_fail("*Actual*: %c\nExpected: %c\n  Colors: %s\n", actual, expected, clrs);
    } else {
        cr_assert(1);
    }
}

// Tests for the color triangle function
Test(Sample_Test, should_return_the_color) {
    assert_data("GB", 'R');
    assert_data("RRR", 'R');
    assert_data("RGBG", 'B');
    assert_data("RBRGBRB", 'G');
    assert_data("RBRGBRBGGRRRBGBBBGG", 'G');
    assert_data("B", 'B');
}


// Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"


// www.codewars.com/r/rvrQdA
