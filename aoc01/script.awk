BEGIN{x=0}
{x=x+$0}
END{print x}
