create or replace PACKAGE user_skills IS


    TYPE skill_data IS RECORD(
        skill_name SKILL.SKILL_NAME%TYPE,
        users_count INTEGER
    );


    TYPE tblskilldata IS TABLE OF skill_data;

    FUNCTION GetSkillData (skill_name SKILL.SKILL_NAME%TYPE default null)
        RETURN tblskilldata
        PIPELINED;


    FUNCTION deleteSkill(skill_name SKILL.SKILL_NAME%TYPE, user_id "user".user_id%type)
    return INTEGER;


    FUNCTION insertSkill(skill_name SKILL.SKILL_NAME%TYPE, user_id "user".user_id%type)
    return INTEGER;

END user_skills;
/



create or replace PACKAGE BODY user_skills IS

    FUNCTION GetSkillData (skill_name SKILL.SKILL_NAME%TYPE default null)
    RETURN tblskilldata
    PIPELINED
    IS

        TYPE skill_cursor_type IS REF CURSOR;
        skill_cursor  skill_cursor_type;

        cursor_data skill_data;
        query_str varchar2(1000);

    begin

        query_str :='select USER_HAS_SKILLS.skill_name, count(USER_HAS_SKILLS.user_id)
                        from USER_HAS_SKILLS
                        where deleted is not null ';

        -- optional part where
            if skill_name is not null then
             query_str:= query_str||' and trim(USER_HAS_SKILLS.skill_name) = trim('''||skill_name||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by USER_HAS_SKILLS.skill_name';



        OPEN skill_cursor FOR query_str;
        LOOP
            FETCH skill_cursor into cursor_data;
            exit when (skill_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetSkillData;


    FUNCTION deleteSkill(skill_name SKILL.SKILL_NAME%TYPE, user_id "user".user_id%type)
        return INTEGER
    is
        begin
            update  USER_HAS_SKILLS
                set DELETED=systimestamp
                where
                    trim(USER_HAS_SKILLS.SKILL_NAME) = trim(skill_name)
                    and
                    USER_HAS_SKILLS.user_id = user_id;
            return 1;
        end;



    FUNCTION insertSkill(skill_name SKILL.SKILL_NAME%TYPE, user_id "user".user_id%type)
        return INTEGER
    is
        is_exists INTEGER:=0;
        begin

            select count(*) into is_exists from  USER_HAS_SKILLS
                where
                    trim(USER_HAS_SKILLS.SKILL_NAME) = trim(skill_name)
                    and
                    USER_HAS_SKILLS.user_id = user_id;

            if   is_exists>0 THEN

                update  USER_HAS_SKILLS
                set DELETED=null
                where
                    trim(USER_HAS_SKILLS.SKILL_NAME) = trim(skill_name)
                    and
                    USER_HAS_SKILLS.user_id = user_id;

                else

                insert into USER_HAS_SKILLS values(skill_name,user_id);

            end if;

            return is_exists;
        end;

END user_skills;
/

