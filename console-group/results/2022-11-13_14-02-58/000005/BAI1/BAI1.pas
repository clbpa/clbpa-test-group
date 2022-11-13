var
  a, b: longint;
  
function gdc(a, b: longint):longint;
begin
  if (b = 0) then exit(a);
  
  exit(gdc(b, a mod b));
end;
  
function lcm(a, b: longint):longint;
begin
  exit((a * b) div gdc(a,b));
end;
  
begin
  readln(a, b);
  
  writeln(gdc(a, b), ' ', lcm(a, b)); 
end.
