#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define magic "cat"

// Check if character is an alphabet or punctuation
int checkWord(char c) {
    return isalpha(c);
}

int main() {

    char sentence[256];
    printf("Enter a sentence, up to 255 characters:\n");
    fgets(sentence, sizeof(sentence), stdin);

    int wordlen = 0;
    char word[20];
    int flag = 0;
    for (int i = 0; i<strlen(sentence); i++) {
        char character = sentence[i]; // Take char by char
        // Can print them by printf "%c"

        // Check if character is an alphabet
        if (checkWord(character)) {
            word[wordlen] = character;
            wordlen++; // Increment index of word
        } else {
            if (wordlen > 0) {  // If exists word already, replace whatever with a NULL and print the word. Accomodates the last '\0'
                word[wordlen] = '\0'; // End the string with \0
                printf("%s \t%d\n",word, wordlen);
            }
            if (strcmp(magic,word)){
                flag = 1;
            }
            wordlen = 0;
        }

    }
    if (flag == 1) {
        printf("You said the magic word!\n");
    }




    return 0;
}