<?xml version="1.0" encoding="UFT-8"?>

<xsl:stylesheet version="1.0"
  xmlns="https://csmp.missouriwestern.edu"
  xmlns:csmp="https://csmp.missouriwestern.edu"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html" doctype-public="XSLT-compat" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />

<xsl:template match="/">
<html>
  <body>
    <h1>Missouri Western State University</h1>
    <h1>College of Liberal Arts and Sciences</h1>
    <h2>Department of Computer Science, Math, and Physics</h2>
    <div class="field"><span class="label">Course Number</span>: <xsl:value-of select="csmp:course/csmp:subject"/> <xsl:value-of select="csmp:course/csmp:number"/></div>
    <div class="field"><span class="label">Course Name</span>: <xsl:value-of select="csmp:course/csmp:title"/></div>

    <xsl:apply-templates select="csmp:course/csmp:prerequisites" />

    <h3>Texbook</h3>
    <xsl:apply-templates select="csmp:course/csmp:textbook" />

    <xsl:apply-templates select="csmp:course/csmp:objectives" />

    <xsl:apply-templates select="csmp:course/csmp:outline" />

  </body>
</html>
</xsl:template>

<xsl:template match="csmp:prerequisites">
  <div class="field"><span class="label">Prerequisites</span>: 
    <xsl:apply-templates select="csmp:prerequisiteCourse" />
  </div>
</xsl:template>

<xsl:template match="csmp:prerequisiteCourse">
  <xsl:value-of select="csmp:subject"/>
  <xsl:value-of select="csmp:number"/>
  <xsl:if test="@corequisite='true'"><xsl:text> (concurrent OK)</xsl:text></xsl:if>
  <xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>&#160;
</xsl:template>

<xsl:template match="csmp:textbook">
  <xsl:value-of select="@title"/>, 
  <xsl:for-each select="csmp:author">
    <xsl:value-of select="current()" />
    <xsl:if test="position() != last()">, </xsl:if>
  </xsl:for-each>;&#160;
  <xsl:if test="@edition != '1'">Edition: <xsl:value-of select="@edition"/>, </xsl:if>
  <xsl:value-of select="@year"/>, 
  <xsl:value-of select="@publisher"/>, 
  ISBN: <xsl:value-of select="@ISBN"/>
</xsl:template>

<xsl:template match="csmp:objectives">
  <h2>Objectives</h2>
  <ul>
    <xsl:apply-templates select="csmp:objective" />
  </ul>
</xsl:template>

<xsl:template match="csmp:objective">
  <li><xsl:value-of select="current()"/></li>
</xsl:template>

<xsl:template match="csmp:outline">
    <h2>Outline</h2>
    <ol>
      <xsl:apply-templates select="csmp:topic" />
    </ol>
</xsl:template>

<xsl:template match="csmp:topic[csmp:topic]">
      <li><xsl:value-of select="text()"/>
        <ol>
          <xsl:apply-templates select="csmp:topic" />
        </ol>
      </li>
</xsl:template>

<xsl:template match="csmp:topic">
      <li><xsl:value-of select="text()"/>
      </li>
</xsl:template>

</xsl:stylesheet>
