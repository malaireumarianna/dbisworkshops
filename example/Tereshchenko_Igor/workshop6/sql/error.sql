create trigger trg_delete_user_skill
  instead of delete on USER_HAS_SKILLS
  REFERENCING OLD AS deleted_row
  FOR EACH ROW
  begin
    deleted_row.deleted:= SYSTIMESTAMP;
  END;