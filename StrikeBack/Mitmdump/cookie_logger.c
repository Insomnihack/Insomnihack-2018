#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

/*
 * Mwahahaha!
 *
 * This scirpt log the cookie recieved from the Set-Cookie of HTTP responses!
 *
 * Example usage:
 * ./cookie_logger "www.npb-bank.ch" "PHPSESSID=0ae08d562bc9a5ab9ab9c737810c6d1a; path=/"
 *
 * [X] TODO_1: i tested it and it logs my own cookies! redact them
 * [X] TODO_2: someone told me they're is a bufer over flaw in the fix of TODO_1?! fix it azap
 * [ ] TODO_3: make it gooder (curently its only working with < 512 chars
 */

// fix for TODO_1, tested working
char* redact(char *buf, char *to_redact) {
  char redacted[512];
  if(strstr(to_redact,"dr-evil"))
    strcpy(redacted,"[REDACTED]");
  else { 
    strcpy(redacted,to_redact);
  }
  strncpy(buf,redacted,512);//fixed the buf over flaw! (TODO_2)
  return buf;
}

// Main 
int main(int argc, char **argv)
{
  char cookie[512];
  char host[512];
  
  //build the csv with a timestamp
  printf("\"%ld\",\"%s\",\"%s\"\n",time(NULL),redact(host,argv[1]),redact(cookie,argv[2]));
}

