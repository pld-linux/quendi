Summary:	electronics conversations
Summary(pl):	elektroniczne konwersacje
Name:		quendi
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Games/Text
Source0:	ftp://aleph-0.dhs.org/people/loth/%{name}-%{version}.tar.gz
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quendi is ideology, but you can treat it like a game. That is useful
to have a conversations with androids and make electronics people. :)

%description -l pl
Projekt pokazuj±cy ¿e grafika nie jest czym¶ koniecznym. ideologiczna
rozmowa z androidem przeklête tworzenie elektronicznych postaci w
krainie ia. Nic specjalnego je¿eli traktujesz to jak grê.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf README ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
