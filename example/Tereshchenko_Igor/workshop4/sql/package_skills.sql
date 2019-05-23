

CREATE OR REPLACE PACKAGE user_skills IS


    TYPE skill_data IS RECORD(
        skill_name SKILL.SKILL_NAME%TYPE,
        users_count INTEGER
    );
    
    
    TYPE tblskilldata IS TABLE OF skill_data;
    
    FUNCTION GetSkillData (skill_name SKILL.SKILL_NAME%TYPE default null)
        RETURN tblskilldata
        PIPELINED;

END user_skills;




CREATE OR REPLACE PACKAGE BODY user_skills IS

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
                        from USER_HAS_SKILLS ';
    
        -- optional part where
            if skill_name is not null then
             query_str:= query_str||' where trim(USER_HAS_SKILLS.skill_name) = trim('''||skill_name||''') ';
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

END user_skills;



