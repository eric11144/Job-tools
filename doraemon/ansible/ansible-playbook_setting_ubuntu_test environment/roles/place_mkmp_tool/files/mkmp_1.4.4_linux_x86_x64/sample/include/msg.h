#ifndef __MSG_H__
#define __MSG_H__

#define DEBUG
#ifdef DEBUG
    #define DBGXXX(L, F, f, l, S, A...) printf("[%s][%s():#%d] " S "\n", F, f, l, ## A)
    #define DBGMSG(S, A...)             DBGXXX(LOG, __FILE__, __func__, __LINE__, S , ## A)
#else
    #define DBGMSG(S, A...)             do {} while (0)
#endif

#endif