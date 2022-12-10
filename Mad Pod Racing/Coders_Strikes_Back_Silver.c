#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef struct io
{
    char    *thrust; // thrust{0..100} or BOOST or SHIELD 
    int     x;
    int     y;
    int     next_checkpt_x;
    int     next_checkpt_y;
    int     dist;
    int     angle;
    int     opponent_x;
    int     opponent_y; 
}   input;

int     init(input *in);


int main()
{
    input   in;
    int     tmp_x;
    int     tmp_y;

    while (1)
    {
        tmp_x = in.x;
        tmp_y = in.y;
        init(&in);

        if (tmp_x == 0)
        {
            tmp_x = in.x;
            tmp_y = in.y;
        }

        if (in.dist < 1500)
            in.thrust = "30";

        if (in.dist < 650)
            in.thrust = "20";
        else
            in.thrust = "100";

        if (abs(in.angle) > 90)
            in.thrust = "0";

        if (in.dist > 5000 && abs(in.angle) < 5)
            in.thrust = "BOOST"; 

        if(in.dist < 500 && hypot(abs(in.x - in.opponent_x), abs(in.y - in.opponent_y)) < 850)
            in.thrust = "SHIELD";

        printf("%d %d %s\n", (in.next_checkpt_x - (in.x - tmp_x) * 3), (in.next_checkpt_y - (in.y - tmp_y) * 3), in.thrust);
    }

    return 0;
}


int init(input *in)
{
    char *thrust = NULL; 
    scanf("%d%d%d%d%d%d"
        , &in->x
        , &in->y
        , &in->next_checkpt_x
        , &in->next_checkpt_y
        , &in->dist
        , &in->angle
    );
    scanf("%d%d"
        , &in->opponent_x
        , &in->opponent_y
    );

    return (1);
}
