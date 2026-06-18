GET /abc123
    ↓
Redis
    ↓
Hit?
  /    \
Yes    No
 |      |
Redirect Postgres
         ↓
      Save Redis
         ↓
      Redirect






  [ Incoming Request ]
                               |
                Is it POST or GET route?
               /                        \
        [ POST /shorten ]          [ GET /{short_code} ]

               |                               |
 Check key: rate:shorten:IP     Check key: rate:redirect:IP
       Limit: 10/min                  Limit: 100/min
               \                        /
             [ Is counter over limit? ]
               /                        \
             Yes                        No
             /                            \
[ Return HTTP 429 ]               [ Process Request ]