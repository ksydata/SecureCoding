/*
SQL Injection 
악의적인 SQL 코드를 어플리케이션 입력 파라미터에 삽입하여
데이터베이스 내 민감정보 접근, 데이터 수정, 시스템 장악
@신다온, 웹 해킹과 취약점 분석, 화이트해커네트웍스, 2024.11.
*/

-- 로그인 폼에서 사용자 ID, PW 입력받을 때 USERNAME 필드에 OR = "1"="1" 입력하면
-- 해당 쿼리는 항상 참이 되어 모든 사용자 정보를 반환
SELECT *
FROM USERS
WHERE USERNAME = "input_username" 
AND PASSWORD = "input_password"


-- 1. 준비된 구문(prepared statements)을 사용
-- SQL쿼리의 구조와 데이터를 분리하여 처리
```php
$stmt = $pdo -> prepare(
"SELECT *
FROM USERS
WHERE USERNAME = :username 
AND PASSWORD = :password"
);
$stmt -> execute(
["username" => $username, 
 "password" => $password]
);```

-- 2. 저장 프로시저를 사용하여 미리 컴파일된 SQL문을 데이터베이스 내에서 실행

-- 3. 입력값(데이터 타입, 길이, 특수문자나 SQL키워드가 포함된 입력) 검증 후 거부/이스케이프 처리
