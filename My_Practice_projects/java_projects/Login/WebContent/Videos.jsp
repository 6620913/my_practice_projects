<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%
   response.setHeader("Cache-Control","no-cache,no-store,must-revalidate");
response.setHeader("Pragma","no-cache");
response.setHeader("Expires","0");
   if(session.getAttribute("username")==null){
	   response.sendRedirect("Login.jsp");
   }

%>
<form action="Logout">
<input type="submit" value="Logout" >
</form>
<br>


Videos are 


<iframe width="560" height="315" src="https://www.youtube.com/embed/OuBUUkQfBYM" ></iframe>

</body>
</html>