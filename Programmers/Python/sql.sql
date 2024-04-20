CREATE TABLE 사원 (
    사원번호 char(6),
    이름 char(20) NOT NULL,
    부서 char(4),
    전화번호 int,
    PRIMARY KEY 사원번호,
    FOREIGN KEY 부서 REFERENCES 부서(부서번호)
);

CREATE TABLE 부서 (
    부서번호 char(4),
    부서명 char(20) NOT NULL,
    부서장 char(6) NOT NULL,
    PRIMARY KEY 부서번호,
    FOREIGN KEY 부서장 REFERENCES 사원(사원번호)
);

CREATE TABLE 업무 (
    사원번호 char(6),
    업무내용 char(20),
    PRIMARY KEY 사원번호, 업무내용
);

SELECT COUNT(*) FROM 사원 WHERE 부서번호 = "L0%";

SELECT 부서.부서명, 업무.업무내용 FROM 업무 INNER JOIN 사원 ON 업무.사원번호 = 사원.사원번호 INNER JOIN 부서 ON 사원.부서 = 부서.부서번호;

ALTER TABLE 사원 ADD 취미 char(20);
UPDATE 사원 SET 취미 = '독서' WHERE 취미 IS NULL;

SELECT 선수.이름, 선수.티어 FROM 소속 INNER JOIN 팀 ON 팀.팀ID = 소속.팀ID INNER JOIN 선수 ON 소속.선수ID = 선수.ID WHERE 팀.팀이름 = 'Miracle';

UPDATE gamer SET tier = "Master"
    WHERE id IN (
        SELECT gamerId FROM team WHERE teamId = (
            SELECT teamId FROM team GROUP BY teamId ORDER BY COUNT(gamerId) ASC LIMIT 1
        )
    )
;

-- 팀 이름이 Miracle 인 팀의 소속 선수들의 이름과 티어를 찾아내는 SQL
SELECT 이름, 티어 FROM 선수 WHERE ID IN (
    SELECT 선수ID FROM 소속 WHERE 팀ID = (
        SELECT 팀ID FROM 팀 WHERE 팀이름 = "Miracle"
    )
)

-- 가장 선수의 숫자가 작은 팀의 모든 선수들의 티어를 '마스터' 로 수정 하는 SQL
UPDATE 선수 SET 티어 = "마스터"
    WHERE ID IN (
        SELECT 선수ID FROM 소속 WHERE 팀ID = (
            SELECT 팀ID FROM 소속 GROUP BY 팀ID ORDER BY COUNT(선수ID) ASC LIMIT 1
        )
    )
;

-- 시합에서 3번 이상 승리한 팀들의 팀이름
SELECT 팀이름 FROM 팀 WHERE 팀ID IN (
    SELECT 승리팀 FROM 시합 GROUP BY 승리팀 HAVING COUNT(시합ID) >= 3
)