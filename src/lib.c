/**
 * lib.c - An testing env for hooks in C
 *
 * Author: Richard Holland
 * Date: 1 Mar 2021
 *
 **/

#include <stdint.h>
#include "../hookapi.h"

int64_t cbak(int64_t reserved)
{
    return 0;
}

int64_t hook(int64_t reserved)
{

  TRACESTR("Accept.c: Called.");
  accept (0,0,0);

  _g(1,1);   // every hook needs to import guard function and use it at least once
  // unreachable
  return 0;
}
