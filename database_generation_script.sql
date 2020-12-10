USE [master]
GO

CREATE DATABASE [name_generator2]
 CONTAINMENT = NONE
GO

USE [name_generator2]
GO

CREATE TABLE [dbo].[name](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[value] [varchar](50) NOT NULL,
	[occurences] [int] NOT NULL,
	[points] [int] NOT NULL,
	[policy] [text] NOT NULL,
	[session] [varchar](150) NOT NULL,
 CONSTRAINT [PK_name] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE VIEW [dbo].[TotalNames]
AS
SELECT TOP (100) PERCENT value, SUM(occurences) AS total
FROM     dbo.name
GROUP BY value
GO

CREATE VIEW [dbo].[TotalNamesByLen]
AS
SELECT LEN(value) AS Expr1, COUNT(value) AS Expr2
FROM     dbo.name
GROUP BY LEN(value)
GO

CREATE TABLE [dbo].[policy](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](500) NOT NULL,
 CONSTRAINT [PK_policy] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[session](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](150) NOT NULL,
	[launched] [datetime] NOT NULL,
	[characters] [varchar](150) NOT NULL,
	[alphabet] [varchar](150) NOT NULL,
 CONSTRAINT [PK_session] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE PROCEDURE [dbo].[GetTotalForLength]
	@nlen int 
AS
SET NOCOUNT ON 
BEGIN
	SELECT * FROM [TotalNames]
	WHERE LEN([value]) = @nlen
	ORDER BY 2 DESC
END
GO

ALTER DATABASE [name_generator2] SET READ_WRITE 
GO
