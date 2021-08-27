package com.Login.dav;
import java.sql.*;

public class LoginDav {
	public LoginDav(){
		
	}

	String sql ="select*from student where name=? and marks=?";
	String url="jdbc:postgresql://localhost:5432/ng";  
	String username = "postgres";
	String passw = "13511351";
	
	public boolean cheak(String uname,String pass){
	try {
	Class.forName("org.postgresql.Driver");
	Connection com = DriverManager.getConnection(url,username,passw);
	PreparedStatement st = com.prepareStatement(sql);
	st.setString(1, uname);
	st.setInt(2,Integer.parseInt(pass));
	ResultSet rs = st.executeQuery();
	if(rs.next()){
		return true;
	}
	}
	catch(Exception e){
		System.out.println(e);
	}

	
	
	return false;
	}
	

}
