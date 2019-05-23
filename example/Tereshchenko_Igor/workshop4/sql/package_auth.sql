

create or replace package user_auth is
    
    function get_user_id(email "user".user_email%type, pass "user".user_password%type)
    return integer;
    
    function is_user(email "user".user_email%type, pass "user".user_password%type)
    return integer;
    
    procedure new_user(
                            user_id OUT integer, 
                            status out varchar2,
                            USER_STUDYBOOK in "user".USER_STUDYBOOK%TYPE,
                            USER_YEAR in "user".USER_YEAR%TYPE,
                            USER_NAME in "user".USER_NAME%TYPE,
                            USER_EMAIL in "user".USER_EMAIL%TYPE,
                            USER_BIRTHDAY in "user".USER_BIRTHDAY%TYPE,
                            USER_PASSWORD in "user".USER_PASSWORD%TYPE
                            );
                            
    
end user_auth;



create or replace package body user_auth is
    
    function is_user(email  "user".user_email%type, pass  "user".user_password%type)
    return integer
    is
        counter INTEGER;
    begin
        select count(*) into counter from "user"
            where 
                trim("user".user_email)=trim(email)
                and
                trim("user".user_password)=trim(pass);
        return counter;        
    end is_user;
    
    function get_user_id(email  "user".user_email%type, pass  "user".user_password%type)
    return integer
    is
        user_id  integer;
    begin
        if is_user(email, pass)>0 then
            
            select "user".user_id into user_id from "user"
            where 
                trim("user".user_email)=trim(email)
                and
                trim("user".user_password)=trim(pass);
                
            return user_id;
        end if;
        return 0;
    end get_user_id;
    
     procedure new_user(
                            user_id OUT integer, 
                            status out varchar2,
                            USER_STUDYBOOK in "user".USER_STUDYBOOK%TYPE,
                            USER_YEAR in "user".USER_YEAR%TYPE,
                            USER_NAME in "user".USER_NAME%TYPE,
                            USER_EMAIL in "user".USER_EMAIL%TYPE,
                            USER_BIRTHDAY in "user".USER_BIRTHDAY%TYPE,
                            USER_PASSWORD in "user".USER_PASSWORD%TYPE
                            )
     is
     begin
     
         --https://docs.oracle.com/cd/B10501_01/appdev.920/a96624/07_errs.htm
     
         BEGIN
            insert into "user"(USER_ID,USER_STUDYBOOK,USER_YEAR,USER_NAME,USER_EMAIL,USER_BIRTHDAY,USER_PASSWORD)
                values(SEQ_USER.nextval, USER_STUDYBOOK,USER_YEAR,USER_NAME,USER_EMAIL,USER_BIRTHDAY,USER_PASSWORD)
            RETURNING USER_ID
                INTO user_id;
                
            COMMIT; 
            status:='ok';
         EXCEPTION 
            WHEN DUP_VAL_ON_INDEX THEN
                status:='user already exists';            
            WHEN OTHERS THEN 
                status:=SQLERRM;
         END;
     end new_user;
    
end user_auth;




