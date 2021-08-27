package com.Login;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.Login.dav.LoginDav;

/**
 * Servlet implementation class Login
 */
@WebServlet("/Login")
public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
 public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	 
	 LoginDav dav = new LoginDav();
	 
	 
 String  uname = request.getParameter("uname");
 String pass = request.getParameter("pass");
 if ( dav.cheak(uname,pass)){
	 response.sendRedirect("Welcom.jsp");
	 HttpSession session = request.getSession();
	 session.setAttribute("username", uname);
 }
 else {
	 response.sendRedirect("Login.jsp");
 }
 
 }

}
